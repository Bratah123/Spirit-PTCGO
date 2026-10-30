from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import destructive_fire, mountain_crush


card = PokemonCardDef(
    guid="21f61cd0-03dc-5aad-804b-9c2491572500",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningTyranitar.Name",
    display_name="Shining Tyranitar",
    searchable_by=["Shining Tyranitar", "Basic", "ShiningTyranitar"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=248,
    abilities=[
        Attack(
            title="Mountain Crush",
            game_text="Flip a coin until you get tails. For each heads, your opponent discards the top card from his or her deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=mountain_crush,
        ),
        Attack(
            title="Destructive Fire",
            game_text="Flip a coin for each Fire Energy card attached to Shining Tyranitar. For each heads, discard a Fire Energy card attached to Shining Tyranitar or this attack does nothing. Then, for each heads, choose an Energy card attached to the Defending Pok\u00e9mon and discard it. If it has fewer Energy cards than that, remove all of them.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FIRE: 3},
            damage=50,
            effect=destructive_fire,
        ),
    ],
)
