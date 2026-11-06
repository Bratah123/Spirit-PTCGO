from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_zoom_passive


card = PokemonCardDef(
    guid="6a685e34-cd42-5261-be19-c18db6bb6872",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownZ.Name",
    display_name="Unown [Z]",
    searchable_by=["Unown [Z]", "Basic", "UnownZ"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Zoom]",
            game_text="As long as Unown [Z] is Benched, you pay no Energy cost to retreat a Pok\u00e9mon with Unown in its name.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_zoom_passive,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
