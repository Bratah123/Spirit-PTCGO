from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import stamp


card = PokemonCardDef(
    guid="1e60cb07-09f6-5466-9d7f-8e61acb839ac",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesRapidash.Name",
    display_name="Blaine's Rapidash",
    searchable_by=["Blaine's Rapidash", "Stage 1", "BlainesRapidash"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesPonyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Stamp",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage (to the Defending Pok\u00e9mon) and 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, this attack does 30 damage (to the Defending Pok\u00e9mon).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=stamp,
        ),
    ],
)
