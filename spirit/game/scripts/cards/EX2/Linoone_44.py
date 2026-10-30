from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import recover_from_discard


card = PokemonCardDef(
    guid="fe4ff75f-091d-5e96-a2c6-fc6a484f9c3d",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1", "Linoone"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Sniff Out",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                count=1, minimum=1, reveal=False, to="hand",
                prompt="Choose a card from your discard pile.",
            ),
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
    ],
)
