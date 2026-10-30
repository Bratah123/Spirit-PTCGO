from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="e7b1d6d9-4ead-541d-b687-161795caccab",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Tail Crush",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
