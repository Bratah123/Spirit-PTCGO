from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ecard import LightweightPassive


card = PokemonCardDef(
    guid="bcc853a4-0628-5409-bb36-863ba8e600f0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    display_name="Hoppip",
    searchable_by=["Hoppip", "Basic", "Hoppip"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=187,
    abilities=[
        Ability(
            title="Lightweight",
            game_text="You pay Colorless less to retreat Hoppip for each Grass Energy attached to it.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=LightweightPassive(),
        ),
        Attack(
            title="Careless Tackle",
            game_text="Hoppip does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=recoil_attack(10),
        ),
    ],
)
