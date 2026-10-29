from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.sm5 import FreezingGazePassive, polar_spear_gx

card = PokemonCardDef(
    guid="ab0d18a5-c3e8-5170-a2b9-a2f96f5bde4c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonGX.Name",
    display_name="Glaceon-GX",
    searchable_by=["Glaceon-GX", "Stage 1", "GX", "GlaceonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=147,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Freezing Gaze",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX in play, in their hand, and in their discard pile have no Abilities, except for Freezing Gaze.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=FreezingGazePassive(),
        ),
        Attack(
            title="Frost Bullet",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Polar Spear-GX",
            game_text="This attack does 50 damage for each damage counter on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=polar_spear_gx,
        ),
    ],
)