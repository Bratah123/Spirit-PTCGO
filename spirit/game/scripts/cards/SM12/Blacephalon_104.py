from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import fireworks_bomb

card = PokemonCardDef(
    guid="ff3625f9-4917-562c-a624-94d6a13b5a89",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blacephalon.Name",
    display_name="Blacephalon",
    searchable_by=["Blacephalon", "Basic", "Ultra Beast", "Blacephalon"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=104,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=806,
    abilities=[
        Attack(
            title="Fireworks Bomb",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like. If your opponent has exactly 3 Prize cards remaining, put 12 damage counters on them instead.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=fireworks_bomb,
        ),
    ],
)