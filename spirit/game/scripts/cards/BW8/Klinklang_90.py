from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9339bc7d-5a33-5b24-8b21-e4556decd011",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Team Plasma", "Klinklang"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=90,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Plasma Steel",
            game_text="Prevent all damage done to your Metal Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Bullet",
            game_text="Flip a coin. If heads, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)