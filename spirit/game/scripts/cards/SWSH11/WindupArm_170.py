from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class WindupArmPassive(Passive):
    """The holder can attack even if it's Asleep or Paralyzed."""

    def attacks_despite_conditions(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonToolCardDef(
    guid="eb68dba7-7f54-5ee1-a0a7-4e94152a92d1",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WindupArm.Name",
    display_name="Windup Arm",
    searchable_by=["Windup Arm", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=170,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    passive=WindupArmPassive(),
)
