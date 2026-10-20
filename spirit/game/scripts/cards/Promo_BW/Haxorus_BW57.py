from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="b377a974-d0cb-5e43-a4e2-3f2dfbdfbaea",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=612,
    abilities=[
        Attack(
            title="Armor Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Dual Chop",
            game_text="Flip 2 coins. This attack does 90 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=90),
        ),
    ],
)