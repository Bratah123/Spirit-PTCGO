from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks

card = PokemonCardDef(
    guid="d170c8ad-2025-5850-aa89-306485591f31",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=79,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            effect=debuff_defender_attacks(20),
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)