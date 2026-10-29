from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage
from spirit.game.card_effects.smp import big_throw_gx


card = PokemonCardDef(
    guid="cdcefae1-d890-537e-93d1-aa877b231586",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BewearGX.Name",
    display_name="Bewear-GX",
    searchable_by=["Bewear-GX", "Stage 1", "GX", "BewearGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=34,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=760,
    abilities=[
        Attack(
            title="Bear Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Double Impact",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=100),
        ),
        Attack(
            title="Big Throw-GX",
            game_text="Discard your opponent's Active Pok\u00e9mon and all cards attached to it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            effect=big_throw_gx,
        ),
    ],
)