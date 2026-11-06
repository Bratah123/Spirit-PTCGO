from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import hurricane


card = PokemonCardDef(
    guid="ab50ad6e-e2b4-57a3-bc80-769eda462a4d",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=18,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Hurricane",
            game_text="Unless this attack Knocks Out the Defending Pok\u00e9mon, return the Defending Pok\u00e9mon and all cards attached to it to your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=hurricane,
        ),
    ],
)
