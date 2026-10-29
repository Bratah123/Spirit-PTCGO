from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack, flip_damage


card = PokemonCardDef(
    guid="24a775fe-587f-5a20-95ec-7ad017928829",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=40),
        ),
    ],
)
