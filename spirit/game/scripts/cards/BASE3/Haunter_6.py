from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import transparency


card = PokemonCardDef(
    guid="947d4b8e-5835-5810-a84a-30989682632d",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Transparency",
            game_text="Whenever an attack does anything to Haunter, flip a coin. If heads, prevent all effects of that attack, including damage, done to Haunter. This power stops working while Haunter is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=transparency,
        ),
        Attack(
            title="Nightmare",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
