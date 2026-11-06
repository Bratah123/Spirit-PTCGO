from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import fire_wind, has_fire_energy_attached


card = PokemonCardDef(
    guid="d9afc570-d45c-5c24-b422-f004352ad0bb",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    display_name="Quilava",
    searchable_by=["Quilava", "Stage 1", "Quilava"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard 1 Fire Energy card attached to Quilava in order to use this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
        Attack(
            title="Fire Wind",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them. Flip 2 coins. For each heads, this attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=fire_wind,
        ),
    ],
)
