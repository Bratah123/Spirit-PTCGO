from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import unnerve_passive


card = PokemonCardDef(
    guid="72fe3440-9ab2-5893-9384-16f1f2624442",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=610,
    abilities=[
        Ability(
            title="Unnerve",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=unnerve_passive,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)