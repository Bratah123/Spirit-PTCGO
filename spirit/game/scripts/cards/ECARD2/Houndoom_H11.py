from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import dark_impact, fireworks


card = PokemonCardDef(
    guid="9f45518f-a0eb-5a40-9dbd-d5b0574b5bd8",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=161,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Houndoom.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=fireworks,
        ),
        Attack(
            title="Dark Impact",
            game_text="The Defending Pok\u00e9mon can't use any Pok\u00e9-Powers until the end of your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=dark_impact,
        ),
    ],
)
