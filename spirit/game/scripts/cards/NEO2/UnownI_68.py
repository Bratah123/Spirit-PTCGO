from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_increase


card = PokemonCardDef(
    guid="7cdea276-24fc-5a2b-be3d-fc0784d74fdf",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownI.Name",
    display_name="Unown [I]",
    searchable_by=["Unown [I]", "Basic", "UnownI"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Increase]",
            game_text="When you play Unown [I] from your hand, you may search your deck for a card with Unown in its name and put it onto your Bench. Shuffle your deck afterward. You can't use this power if your Bench is full.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=unown_increase,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
