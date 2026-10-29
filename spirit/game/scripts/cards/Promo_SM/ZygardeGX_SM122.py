from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.smp import liberation_gx


card = PokemonCardDef(
    guid="5a96fb64-d01d-5301-962a-7f4222ed7189",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=122,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Vibration",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Cell Storm",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=heal_attack(30, target='self'),
        ),
        Attack(
            title="Liberation-GX",
            game_text="Your opponent reveals their hand. This attack does 120 damage for each Energy card you find there. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="x",
            effect=liberation_gx,
        ),
    ],
)