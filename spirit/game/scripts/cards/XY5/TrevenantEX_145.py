from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, count_energy


card = PokemonCardDef(
    guid="118fea69-fece-59a2-be6d-04ed32600b05",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantEX.Name",
    display_name="Trevenant-EX",
    searchable_by=["Trevenant-EX", "Basic", "EX", "TrevenantEX"],
    subtypes=["Basic", "EX"],
    collector_number=145,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=709,
    abilities=[
        Attack(
            title="Dark Forest",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Wood Blast",
            game_text="This attack does 20 more damage for each Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.GRASS), 20, base=50),
        ),
    ],
)