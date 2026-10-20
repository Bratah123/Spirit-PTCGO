from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play


card = PokemonCardDef(
    guid="1be6848c-90b3-5a4f-a4b8-50382e852303",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonBREAK.Name",
    display_name="Empoleon BREAK",
    searchable_by=["Empoleon BREAK", "BREAK", "EmpoleonBREAK"],
    subtypes=["BREAK"],
    collector_number=134,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    family_id=395,
    abilities=[
        Attack(
            title="Emperor's Command",
            game_text="This attack does 30 damage times the number of Pok\u00e9mon your opponent has in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play('opponent'), 30),
        ),
    ],
)