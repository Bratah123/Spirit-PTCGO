from spirit.game.card_effects.attacks_common import bonus_if, count_energy
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

_extra_fighting_energy = lambda ctx: count_energy(
    "self", energy_type=PokemonTypes.FIGHTING)(ctx) >= 3

card = PokemonCardDef(
    guid="e820b680-0fd1-5cbc-bcf2-f509b9950590",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1", "Sandaconda"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Ability(
            title="Sand Sac",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Power Press",
            game_text="If this Pok\u00e9mon has at least 1 extra Fighting Energy attached (in addition to this attack's cost), this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_extra_fighting_energy, 70),
        ),
    ],
)