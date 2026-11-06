from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import burning_fire


card = PokemonCardDef(
    guid="da1bf7db-3f6b-5328-9e2b-536f3efb13b1",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Burning Fire",
            game_text="When you use this attack, you may discard any number of Fire Energy cards attached to your Pok\u00e9mon in play. This attack does 10 damage plus 10 more damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=burning_fire,
        ),
        Attack(
            title="Magma Punch",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
