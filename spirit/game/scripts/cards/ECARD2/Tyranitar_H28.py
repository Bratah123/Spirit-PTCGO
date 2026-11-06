from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import destructive_roar, gigacrush


card = PokemonCardDef(
    guid="9581f73c-5ec7-5e6a-a7fc-1c85d0a2fdc4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=178,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Destructive Roar",
            game_text="Flip a coin. If heads, discard 1 Energy card attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=destructive_roar,
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Gigacrush",
            game_text="Each player discards the top 3 cards from his or her deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=gigacrush,
        ),
    ],
)
