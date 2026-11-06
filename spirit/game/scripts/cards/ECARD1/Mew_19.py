from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import super_psywave


card = PokemonCardDef(
    guid="295b88e2-9ccd-569d-bf51-2b140f3d8213",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Super Psywave",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Count the number of Energy cards attached to that Pok\u00e9mon. Put that many damage counters on the Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=super_psywave,
        ),
    ],
)
