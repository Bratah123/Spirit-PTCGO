from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_per, count_bench, flip_damage, condition_attack


def _is_fire_pokemon(card):
    return PokemonTypes.FIRE.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="33f61adf-d462-5d97-a05b-5dcfff32361c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarGX.Name",
    display_name="Incineroar-GX",
    searchable_by=["Incineroar-GX", "Stage 2", "GX", "IncineroarGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=38,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Hustling Strike",
            game_text="This attack does 20 more damage for each of your Benched Fire Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench('mine', pred=_is_fire_pokemon), 20, base=10),
        ),
        Attack(
            title="Tiger Swing",
            game_text="Flip 2 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=50),
        ),
        Attack(
            title="Burning Slam-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)