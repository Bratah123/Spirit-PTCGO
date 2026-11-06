from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_or_nothing


card = PokemonCardDef(
    guid="c70369c0-0e80-51c3-aa55-2748cf8710ef",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1", "Rhydon"],
    subtypes=["Stage 1"],
    collector_number=177,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=flip_or_nothing(),
        ),
    ],
)
