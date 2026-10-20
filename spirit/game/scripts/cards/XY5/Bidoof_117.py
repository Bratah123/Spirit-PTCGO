from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import bonus_if, count_energy


card = PokemonCardDef(
    guid="971f22bc-2a67-59c4-a08e-cf54638b5e93",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    display_name="Bidoof",
    searchable_by=["Bidoof", "Basic", "Bidoof"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=399,
    abilities=[
        ancient_trait('α Recovery'),
        Attack(
            title="Drench",
            game_text="If this Pok\u00e9mon has any Water Energy attached to it, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_energy('self', energy_type=PokemonTypes.WATER)(ctx) > 0, 20),
        ),
    ],
)