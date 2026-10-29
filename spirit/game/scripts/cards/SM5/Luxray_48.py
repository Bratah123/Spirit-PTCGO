from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sl import IntimidatingPatternPassive
from spirit.game.card_effects.sm5 import volt_bolt

card = PokemonCardDef(
    guid="6164397e-2c24-53b7-8b59-0e53f63d5759",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=IntimidatingPatternPassive(),
        ),
        Attack(
            title="Volt Bolt",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon. This attack does 150 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=volt_bolt,
        ),
    ],
)