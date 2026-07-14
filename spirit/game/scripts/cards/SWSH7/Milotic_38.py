from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import trainer_effect_shield_passive


def _you_or_your_hand(entity, carrier):
    # "done to you or your hand": player-level effects plus cards in hand;
    # effects on your Pokemon (Boss's Orders, damage) are NOT prevented.
    if entity is None:
        return True
    parent = getattr(entity, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "hand"

card = PokemonCardDef(
    guid="11050f75-e444-53ac-af9b-8803477130eb",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Rapid Strike", "Milotic"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=38,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Dew Guard",
            game_text="Whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to you or your hand.",
            passive=trainer_effect_shield_passive(protects=_you_or_your_hand),
        ),
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=70),
        ),
    ],
)