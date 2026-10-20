from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="41b3f92a-5099-5420-8a29-3e1785343aa2",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Beckon",
            game_text="Put a Supporter card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=recover_from_discard(predicate=is_supporter_card, count=1, minimum=1, reveal=True, to="hand"),
        ),
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)