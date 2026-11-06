from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import hyper_flame


card = PokemonCardDef(
    guid="55792970-2f0a-51dd-9759-78188de43b81",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Hyper Flame",
            game_text="Flip a coin. If heads, discard 1 Fire Energy card attached to Moltres. If tails, discard all Energy cards attached to Moltres. If you can't discard Energy cards, this attack does nothing.",
            cost={PokemonTypes.FIRE: 3},
            damage=60,
            effect=hyper_flame,
        ),
    ],
)
