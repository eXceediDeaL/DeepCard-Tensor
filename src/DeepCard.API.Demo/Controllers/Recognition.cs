using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace DeepCard.API.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class RecognitionController : ControllerBase
    {
        [HttpPost]
        public ActionResult<string> Recognize([FromBody] string image)
        {
            return "00000000000000000";
        }
    }
}
