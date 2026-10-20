from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="b9884cf2-d2b3-5dba-8fc8-83f3e9f9b8be",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XerneasBREAK.Name",
    display_name="Xerneas BREAK",
    searchable_by=["Xerneas BREAK", "BREAK", "XerneasBREAK"],
    subtypes=["BREAK"],
    collector_number=82,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    family_id=716,
    abilities=[
        Attack(
            title="Life Stream",
            game_text="This attack does 20 damage times the amount of Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy('mine'), 20),
        ),
    ],
)