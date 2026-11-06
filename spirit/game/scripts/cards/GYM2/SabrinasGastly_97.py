from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import gaseous_form_passive


card = PokemonCardDef(
    guid="ed8120bc-7f39-5e4f-82af-4adedaab662a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGastly.Name",
    display_name="Sabrina's Gastly",
    searchable_by=["Sabrina's Gastly", "Basic", "SabrinasGastly"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Ability(
            title="Gaseous Form",
            game_text="Sabrina's Gastly gets +10 HP for each Psychic Energy card attached to it. This power works even if Sabrina's Gastly is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=gaseous_form_passive,
        ),
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)
