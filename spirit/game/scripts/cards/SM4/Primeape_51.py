from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import lucha_fight

card = PokemonCardDef(
    guid="922d7854-73de-5b5c-ba27-32d854282807",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Lucha Fight",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            effect=lucha_fight,
        ),
    ],
)