from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import electric_bolt, lock_on


card = PokemonCardDef(
    guid="3e94f7c3-7d43-5c5e-9081-d873d5e73090",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=81,
    abilities=[
        Attack(
            title="Lock-on",
            game_text="During your next turn, treat any tails flipped when using Magnemite's Electric Bolt attack as if they were heads. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lock_on,
        ),
        Attack(
            title="Electric Bolt",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Paralyzed. If either of them is tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=electric_bolt,
        ),
    ],
)
