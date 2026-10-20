from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="59999993-d1fd-5071-8780-a9c11b03bcb4",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Softboiled",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, heal 30 damage from your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon does 60 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
    ],
)