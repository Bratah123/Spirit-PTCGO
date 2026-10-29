from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.smp import enraged_strike, familial_combo_gx


card = PokemonCardDef(
    guid="64ebe692-9f18-59ff-8900-9f75ad4dd1e9",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KangaskhanGX.Name",
    display_name="Kangaskhan-GX",
    searchable_by=["Kangaskhan-GX", "Basic", "GX", "KangaskhanGX"],
    subtypes=["Basic", "GX"],
    collector_number=188,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Split Spiral Punch",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Enraged Strike",
            game_text="If your opponent's Active Pok\u00e9mon is Confused, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=enraged_strike,
        ),
        Attack(
            title="Familial Combo-GX",
            game_text="Draw 5 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=familial_combo_gx,
        ),
    ],
)