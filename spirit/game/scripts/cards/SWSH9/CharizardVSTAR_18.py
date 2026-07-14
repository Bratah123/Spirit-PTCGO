from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage, self_energy_discard_attack

card = PokemonCardDef(
    guid="717356f0-1dfd-5477-aa96-08d899d4b142",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardVSTAR.Name",
    display_name="Charizard VSTAR",
    searchable_by=["Charizard VSTAR", "VSTAR", "CharizardVSTAR"],
    subtypes=["VSTAR"],
    collector_number=18,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVSTAR,
    hp=280,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Explosive Fire",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=bonus_if(has_damage("self"), 100),
        ),
        Attack(
            title="Star Blaze",
            game_text="Discard 2 Energy from this Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=320,
            vstar=True,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)