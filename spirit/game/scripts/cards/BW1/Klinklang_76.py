from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c4b694a1-3bba-5ee5-a1e0-80d5582db182",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="BW1",
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
            title="Shift Gear",
            game_text="As often as you like during your turn (before your attack), you may move a Metal Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Gear Grind",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)