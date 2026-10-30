from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import evolution_song


card = PokemonCardDef(
    guid="96f92ffa-33ae-55ae-868c-b26cf5f4fbca",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightWigglytuff.Name",
    display_name="Light Wigglytuff",
    searchable_by=["Light Wigglytuff", "Stage 1", "LightWigglytuff"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Evolution Song",
            game_text="Your opponent may choose 1 of his or her Pok\u00e9mon and search his or her deck for a card that evolves from that Pok\u00e9mon. Your opponent attaches that card to that Pok\u00e9mon. This counts as evolving that Pok\u00e9mon. Either way, you may do the same, and then each player who searched shuffles his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=evolution_song,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
