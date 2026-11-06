from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="7123bf05-34a8-5f4d-9b4c-943544fd50ed",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesDodrio.Name",
    display_name="Blaine's Dodrio",
    searchable_by=["Blaine's Dodrio", "Stage 1", "BlainesDodrio"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesDoduo.Name",
    family_id=84,
    abilities=[
        Attack(
            title="Mega Peck",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)
