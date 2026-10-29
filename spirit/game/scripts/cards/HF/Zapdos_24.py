from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.hf import hurricane_call

card = PokemonCardDef(
    guid="020e6697-16bd-51cd-a0e8-dfcc73c2f9ab",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=145,
    abilities=[
        Attack(
            title="Hurricane Call",
            game_text="Flip 4 coins. For each heads, search your deck for a Lightning Energy card and attach it to 1 of your Pok\u00e9mon-GX or Pok\u00e9mon-EX. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=hurricane_call,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
