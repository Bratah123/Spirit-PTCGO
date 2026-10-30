from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import wildfire


card = PokemonCardDef(
    guid="8df03dc8-3369-56f0-8b11-1cca28250491",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Wildfire",
            game_text="You may discard any number of Fire Energy cards attached to Moltres when you use this attack. If you do, discard that many cards from the top of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=wildfire,
        ),
        Attack(
            title="Dive Bomb",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 4},
            damage=80,
            effect=flip_or_nothing(),
        ),
    ],
)
