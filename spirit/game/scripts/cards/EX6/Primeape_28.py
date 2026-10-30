from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import toss_tm_tools

card = PokemonCardDef(
    guid="80e8c911-3140-5270-82aa-07b6313f0c7e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Toss",
            game_text="You may discard from your hand as many Technical Machine and Pok\u00e9mon Tool cards as you like. This attack does 30 damage times the number of cards you discarded.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=toss_tm_tools(30),
        ),
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)