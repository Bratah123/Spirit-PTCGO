from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_hand
from spirit.game.card_effects.sm4 import chaos_wheel


card = PokemonCardDef(
    guid="b6518f64-af46-5cf4-b65c-491ae7f14d06",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Attack(
            title="Chaos Wheel",
            game_text="Your opponent can't play any Pok\u00e9mon Tool, Special Energy, or Stadium cards from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=chaos_wheel,
        ),
        Attack(
            title="Dark Arts",
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=damage_per(count_hand('opponent'), 20),
        ),
    ],
)