from spirit.game.card_effects.pokemon import WaveVeilPassive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe53515c-30ea-5867-bd89-f4ee7b6fc52c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Wave Veil",
            game_text="Prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon.",
            passive=WaveVeilPassive(),
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
