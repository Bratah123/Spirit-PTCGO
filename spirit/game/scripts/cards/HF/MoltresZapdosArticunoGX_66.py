from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.hf import sky_legends_gx

card = PokemonCardDef(
    guid="2e1b2da9-649a-50d0-a2ae-9b5e6dce003b",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresZapdosArticunoGX.Name",
    display_name="Moltres & Zapdos & Articuno-GX",
    searchable_by=["Moltres & Zapdos & Articuno-GX", "Basic", "TAG TEAM", "GX", "MoltresZapdosArticunoGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=66,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Attack(
            title="Trinity Burn",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=210,
        ),
        Attack(
            title="Sky Legends-GX",
            game_text="Shuffle this Pok\u00e9mon and all cards attached to it into your deck. If this Pok\u00e9mon has at least 1 extra Fire, Water, and Lightning Energy attached to it (in addition to this attack's cost), this attack does 110 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sky_legends_gx,
        ),
    ],
)
