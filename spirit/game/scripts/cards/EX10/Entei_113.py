from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import star_turn_switch, detonation_mill

card = PokemonCardDef(
    guid="9a8eb953-5a26-5997-a968-357c73a5a732",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei ★",
    searchable_by=["Entei \u2605", "Basic", "Star", "Entei"],
    subtypes=["Basic", "Star"],
    collector_number=113,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Burning Turn",
            game_text="Switch Entei Star with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=star_turn_switch(20),
        ),
        Attack(
            title="Detonation",
            game_text="If you have less Prize cards left than your opponent, discard the top 10 cards from your deck.",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            effect=detonation_mill(70, 10),
        ),
    ],
)
