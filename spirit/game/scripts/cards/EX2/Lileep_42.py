from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import search_to_bench_named, time_spiral


card = PokemonCardDef(
    guid="31d5f259-b2be-587c-bed1-626c0608ac5a",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Stage 1", "Lileep"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Influence",
            game_text="Search your deck for Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith and put up to 2 of them onto your Bench. Shuffle your deck afterward. Treat the new Benched Pok\u00e9mon as Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench_named(
                "Omanyte", "Kabuto", "Aerodactyl", "Lileep", "Anorith",
                count=2,
                prompt="Choose up to 2 of Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith to put onto your Bench.",
            ),
        ),
        Attack(
            title="Time Spiral",
            game_text="If your opponent has any Evolved Pok\u00e9mon in play, choose 1 of them and flip a coin. If heads, remove the highest Stage Evolution card on that Pok\u00e9mon and have your opponent shuffle it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=time_spiral,
        ),
    ],
)
